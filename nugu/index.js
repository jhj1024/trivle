const uuid = require('uuid').v4
const _ = require('lodash')
const { DOMAIN } = require('../config')
var mysql = require('mysql');
var dbconfig = require('../database.js');
var pool = mysql.createPool(dbconfig);

function throwDice(diceCount) {
    var sum = 3;
    var diceCount = 1;
    pool.getConnection(function(err, connection) {
        var sqlForCart = "SELECT * FROM trivel.clothes;";
        connection.query(sqlForCart, function(err, rows) {
            if (err) {
                console.log('err :' + err);
                var midText = "NO"
            } 
            else {
                var midText = "OK"
            }
        })
    });

    return {midText, sum, diceCount}
}


class NPKRequest {
  constructor (httpReq) { //httpReq의 body에 context와 action이 옴(도큐먼트 참조)
    this.context = httpReq.body.context
    this.action = httpReq.body.action
    console.log(`NPKRequest: ${JSON.stringify(this.context)}, ${JSON.stringify(this.action)}`)
  }
  
  //reqeust 처리
  do(npkResponse) { 
    this.actionRequest(npkResponse)
  }
  actionRequest(npkResponse) {
    console.log('actionRequest')
    console.dir(this.action)

    //액션 이름과 파라미터 저장(모두 nugu play kit의 액션과 파라미터 이름임)
    const actionName = this.action.actionName 
    const parameters = this.action.parameters

    switch (actionName) {
    case 'ThrowDiceAction' || 'ThrowYesAction':
      let diceCount = 1 //entity가 필수가 아닌 경우 default로 개수 정해둠
      if (!!parameters) {
        const diceCountSlot = parameters.diceCount //파라미터 중 하나인 diceCount
        if (parameters.length != 0 && diceCountSlot) {
          diceCount = parseInt(diceCountSlot.value)
        }

        if (isNaN(diceCount)) {
          diceCount = 1
        }
      }
      const throwResult = throwDice(diceCount) //주사위를 던지는 함수 throwDice실행하여 결과를 throwResult에 저장
      npkResponse.setOutputParameters(throwResult) //response output parameter set
      break
    }
  }
}

class NPKResponse {
  constructor () {
    console.log('NPKResponse constructor')
    this.version = '2.0'
    this.resultCode = 'OK'
    this.output = {}
    this.directives = []
  }

  setOutputParameters(throwResult) { //response out 규격 즉, 결과 파라미터 저장
    this.output = {
      diceCount: throwResult.diceCount,
      sum: throwResult.sum,
      midText: throwResult.midText,
    }
  }
}


const nuguReq = function (httpReq, httpRes, next) {
  npkResponse = new NPKResponse()
  npkRequest = new NPKRequest(httpReq) //nugu play kit의 request
  npkRequest.do(npkResponse) //결과를 npkResponse에 담음
  console.log(`NPKResponse: ${JSON.stringify(npkResponse)}`) 
  return httpRes.send(npkResponse) //전송
};

module.exports = nuguReq;