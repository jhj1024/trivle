const uuid = require('uuid').v4
const _ = require('lodash')
const { DOMAIN } = require('../config')
var mysql = require('mysql');
var dbConfig = {
 host     : '45.119.146.152',
    user     : 'trivle',//계정 아이디
    password : 'Trivle_96',//계정 비번
    port     : 1024,
    database : 'trivle'//접속할 디비
};
var pool = mysql.createPool(dbConfig);

//--------------------------------------------------------------
function Start(DestinationForSet) {
    let exist = 0
    /////////////디비에 저장되어 있는 리스트인지 확인/////////////////
    var mysql = require('mysql');//mysql 모듈 불러오기
    //mysql 커넥션 생성
    var connection = mysql.createConnection({
    host     : '45.119.146.152',
    user     : 'trivle',//계정 아이디
    password : 'Trivle_96',//계정 비번
    port     : 1024,
    database : 'trivle'//접속할 디비
    });
    connection.connect();//mysql 접속
   //리스트가 만들어진 여행장소를 location 테이블에 저장했다고 가정
    connection.query('SELECT * from location', function(err, rows) {
        if (!err){
            if(rows.length == 0)
                exist = 0
            else{
                for(var i=0; i<rows.length;i++){
                    if(rows[i].L == DestinationForSet)
                        exist = 1
                }
            }
        }
        else
            console.log('Error while performing Query.', err);
    });
    connection.end();
    ////////////기존 리스트에 있는 경우////////////
    if(exist == 1)
        Read(DestinationForSet);
    ////////////기존 리스트에 없는 경우////////////
    else
       New(DestinationForSet, DestinationForSet.type);
}

function Listen_Tip(DestinationForSet){
    let Tip = '';
    /////////////디비에 저장되어 있는 리스트인지 확인/////////////////
    var mysql = require('mysql');//mysql 모듈 불러오기
    //mysql 커넥션 생성
    var connection = mysql.createConnection({
    host     : '45.119.146.152',
    user     : 'trivle',//계정 아이디
    password : 'Trivle_96',//계정 비번
    port     : 1024,
    database : 'trivle'//접속할 디비
    });
    connection.connect();//mysql 접속
    
    connection.query('SELECT * from T', function(err, rows) {
        if (!err){
                const rand = Math.floor(Math.random() * 8);
                Tip = rows[rand].T;
                console.log(Tip);
                return {Tip};
        }
        else
            console.log('Error while performing Query.', err);
    });
    connection.end();
}

function Set_List(DestinationForSet) { //몇박몇일에 대한 데이터도 인자로 추가
  const hey = DestinationForSet.type; //국내/해외인지 엔티티 타입(in/ hey)
  const Destination = DestinationForSet.value; //여행지 이름 (런던, 파리, 강원도)
  console.log('DestinationForSet: ' + Destination); 
  /*
  pool.getConnection(function(err, connection) {
    if(err){
      console.log('DB_connection_err :' + err);
    }
    else{
      var sqlForCart = "SELECT * FROM clothes;";
      connection.query(sqlForCart, function(err, rows) {
        if (err) {
          console.log('query_err :' + err);
          
        } 
        else {
          
        }
      })
    }
  })
  */
  return {Destination}
}

function Delete_List(DestinationForDelete) {
  const Destination = DestinationForDelete;
  console.log('DestinationForDelete: ' + Destination); 
  /*
  pool.getConnection(function(err, connection) {
    if(err){
      console.log('DB_connection_err :' + err);
    }
    else{
      var sqlForCart = "SELECT FROM  WHERE";
      connection.query(sqlForCart, function(err, rows) {
        if (err) {
          console.log('query_err :' + err);
          
        } 
        else {
          
        }
      })
    }
  })
  */
  return {Destination}
}

function Listen_List(DestinationForListen) { //읽을 카테고리 데이터도 인자로 추가
  const Destination = DestinationForListen;
  console.log('DestinationForListen: 하이하이^^ ' + Destination); 
  /*
  pool.getConnection(function(err, connection) {
    if(err){
      console.log('DB_connection_err :' + err);
    }
    else{
      var sqlForCart = "SELECT FROM  WHERE";
      connection.query(sqlForCart, function(err, rows) {
        if (err) {
          console.log('query_err :' + err);          
        } 
        else {
          
        }
      })

    }

  })
  */
  return {Destination}
}

//--------------------------------------------------------------
class NPKRequest {
  constructor (httpReq) { //httpReq의 body에서 context와 action 추출
    console.log(httpReq.body)
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
    let result = null

    switch (actionName) {
      case 'Set_List':
      let DestinationForSet = parameters.DestinationForSet //여행지
      //몇박몇일에 대한 데이터도 파라미터로 추가 

      result = Set_List(DestinationForSet.value) //함수 실행
      console.log(result)
      npkResponse.Set_List_Output(result) //함수 결과를 output 파라미터에 저장
      break;

      case 'Delete_List':
      const DestinationForDelete = parameters.DestinationForDelete //여행지
      
      result = Delete_List(DestinationForDelete) //함수 실행
      console.log(result)
      npkResponse.Delete_List_Output(result) //함수 결과를 output 파라미터에 저장
      break;

      case 'Listen_List':
      const DestinationForListen = parameters.DestinationForListen //여행지
      //읽을 카테고리 데이터도 파라미터로 추가

      result = Listen_List(DestinationForListen.value) //함수 실행
      console.log(result)
      npkResponse.Listen_List_Output(result) //함수 결과를 output 파라미터에 저장
      break;
            
      case 'Listen_Tip':
      result = Listen_Tip(DestinationForSet) //함수 실행
      console.log(result)
      console.log('@@@@@@@')
      npkResponse.Listen_Tip_Output(result) //함수 결과를 output 파라미터에 저장
      break;
            
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

  //function 결과 파라미터 규격 설정
  Set_List_Output(result) {
    this.output = {
      Destination1: result.Destination
    }
  }

  Delete_List_Output(result) {
    this.output = {
      Destination2: result.Destination
    }
  }

  Listen_List_Output(result) {
    this.output = {
      Destination3: result.Destination
    }
  }

  Listen_Tip_Output(result) {
    this.output = {
      TIP: result.Tip,
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