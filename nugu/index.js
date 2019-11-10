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
//let TIP = ""; 
//SY--------------------------------------------------------------
function Start(DestinationForSet) {
    let exist = 0
    /////////////디비에 저장되어 있는 리스트인지 확인/////////////////
    
   //리스트가 만들어진 여행장소를 location 테이블에 저장했다고 가정
    pool.getConnection(function(err, connection) {
        if (err)
            console.log('Error while performing Query.', err);
        else{
            var sqlForStart = "SELECT * from location";
            connection.query(sqlForStart, function(err, rows){
                if(err){
                    console.log('Error while performing Query.', err);
                }
                else{
                    if(rows.length == 0)
                        exist = 0
                    else{
                        for(var i=0; i<rows.length;i++){
                            if(rows[i].L == DestinationForSet)
                                exist = 1
                        }
                    }
                }
            })
        }
    });
    ////////////기존 리스트에 있는 경우////////////
    if(exist == 1)
        Read(DestinationForSet);
    ////////////기존 리스트에 없는 경우////////////
    else
       Make_List(DestinationForSet, DestinationForSet.type);
}

//JH------------------------------------
function Make_List(DestinationForSet, Type){
  
  console.log('DestinationForMake: ' + Destination); 
  if(Type = "IN") //국내인경우
  {
      Make_In(DestinationForset,FewDay);
  }
  else //해외인경우
  {
      Make_Out(DestinationForset,FewDay);
  }
}

function Make_In(DestinationForset,FewDay)
{
  
  console.log('MakeIn: ' + Destination); 
  if(FewDay<=7)
  {
      Make_In_Short();
  }
  else
  {
      Make_In_Long();
  }
}


function Make_Out(DestinationForset,FewDay)
{
  
  console.log('MakeOut: ' + Destination); 
  if(FewDay<=7)
  {
      Make_Out_Short();
  }
  else
  {
      Make_Out_Long();
  }
}

//생성 함수
function Make_In_Short(DestinationForset,FewDay)
{
  
  console.log('MakeInShort: ' + Destination); 

  var sql = 'Create table ? SELECT * FROM IS where = ?;'

  pool.getConncetion(function(err, connection) {
      connection.query(sql, DestinationForset, function(err, rows) {
        if (err) {
          console.log('Error Create Query.', err);
        } 
        else {
          console.log("Create table");
        }
      });
  })
}

function Make_In_Long(DestinationForset,FewDay)
{
  
  console.log('MakeInLong: ' + Destination); 
  var sql = 'Create table ? SELECT * FROM IL where = ?;'

  pool.getConncetion(function(err, connection) {
      connection.query(sql, DestinationForset, function(err, rows) {
        if (err) {
          console.log('Error Create Query.', err);
        } 
        else {
          console.log("Create table");
        }
      });
  })
}

function Make_Out_short(DestinationForset,FewDay)
{
  
  console.log('MakeOutShort: ' + Destination); 
  var sql = 'Create table ? SELECT * FROM OS where = ?;'

  pool.getConncetion(function(err, connection) {
      connection.query(sql, DestinationForset, function(err, rows) {
        if (err) {
          console.log('Error Create Query.', err);
        } 
        else {
          console.log("Create table");
        }
      });
  })
}

function Make_Out_Long(DestinationForset,FewDay)
{
  
  console.log('MakeOutLong: ' + Destination); 
  var sql = 'Create table ? SELECT * FROM OL where = ?;'

  pool.getConncetion(function(err, connection) {
      connection.query(sql, DestinationForset, function(err, rows) {
        if (err) {
          console.log('Error Create Query.', err);
        } 
        else {
          console.log("Create table");
        }
      });
  })
}

function Delete_List(DestinationForDelete) {

  const Destination = DestinationForDelete;
  console.log('DestinationForDelete: ' + Destination); 

  var sql = 'Delete FROM ? where = ?;'

  pool.getConncetion(function(err, connection) {
      connection.query(sql, DestinationForset, function(err, rows) {
        if (err) {
          console.log('Error Create Query.', err);
        } 
        else {
          console.log("Create table");
        }
      });
  })

  return {Destination}
}
//--------------------------------------------------

//SY------------------------------------------------
function Listen_Tip(){
    //let Destination = DestinationForTip;
    
    let TIP ='시러~';
    //var TIP = ""; 
    pool.getConnection(function(err, connection) {
        if (err)
            console.log('Error while performing Query.', err);
        else{
            var sqlForTip = "SELECT * from T";
            connection.query(sqlForTip, function(err, rows){
                const rand = Math.floor(Math.random() * 8);
                TIP = rows[rand].T;

                console.log('1' + TIP);
            })
        }
    });

    console.log('2'+TIP);

    return {TIP};
}


function Listen_List(DestinationForListen) { //읽을 카테고리 데이터도 인자로 추가
  let Destination = DestinationForListen;
  var listen = '다쿠아즈';

  console.log('Destination: ' + Destination); 
  console.log('Destination type: ' + typeof(Destination)); 

  pool.getConnection(function(err, connection) {
    if(err){
      console.log('DB_connection_err :' + err);
    }
    else{
      var sqlForListen = "SELECT * FROM " + Destination + ";"
      connection.query(sqlForListen, function(err, rows) {
        if (err) {
          console.log('query_err :' + err);          
        } 
        else {
          console.log(rows[0])
          listen = rows[0].P     
        }
      })

    }

  })
  return {listen} 
}

//--------------------------------------------------------------
class NPKRequest {
  constructor (httpReq) { //httpReq의 body에서 context와 action 추출
    //console.log(httpReq.body)
    this.context = httpReq.body.context
    this.action = httpReq.body.action
    //console.log(`NPKRequest: ${JSON.stringify(this.context)}, ${JSON.stringify(this.action)}`)
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

    console.log('액션먼저?')
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

      const result1 = await Listen_List(DestinationForListen.value) //함수 실행
      console.log('함수결과' + result1.listen)
      npkResponse.Listen_List_Output(result1) //함수 결과를 output 파라미터에 저장
      break;
            
      case 'Listen_Tip':
      //const DestinationForTip = parameters.DestinationForTip //여행지
      console.log('어떤거 먼저?')
      result = callback(Listen_Tip()) //함수 실행
      console.log('3'+result)
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
      Destination1: result.DestinationForset
    }
  }

  Delete_List_Output(result) {
    this.output = {
      Destination2: result.Destination
    }
  }

  Listen_List_Output(result) {
    this.output = {
      Destination3: result.listen
    }
  }

  Listen_Tip_Output(result) {
    this.output = {
      TIP: result.TIP
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