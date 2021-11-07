const quiz = document.querySelector("#quest");

var data = []

var calculateModel = function () {
  fetch('/'+ data)
  .then(response => {
    return response.json();
  })
  .then(data => {
    console.log(data[0])
    let result = document.querySelector('.result')
    result.innerHTML = ""
    result.appendChild(document.createTextNode("O seu desempenho médio no ENEM nas provas objetivas será de: "+
                                               (1000*data[0]).toFixed(2) + 
                                               ". O seu desempenho na nota de redação será: " +
                                               (1000*data[1]).toFixed(2)))
  });
}


var none = function(e) {
  e.path[3].classList.add("null");
  e.path[3].nextSibling.classList.remove("null");
  data.push(parseFloat(e.path[0].value)); 

  if (e.path[3].nextSibling.classList.contains("result")){
    console.log(data)
    calculateModel()
  }
}




var addQuestsJson = function(json){
  let count = 1
  let t = false
  for(let i in json){
    if (count ==  14 || count == 22 || count == 24 || count == 25 || count ==27){
      count++;
    } 
    else{
      let quest = document.createElement("div")
      quest.classList.add("quest")
      let p = document.createElement('p')
      p.appendChild(document.createTextNode(i))
      quest.appendChild(p)
      for(let j in json[i]){
        let answer = document.createElement('span')
        answer.classList.add("answer")
        let d = document.createElement('div')
        let input = document.createElement("input")
        input.setAttribute("type","radio")
        input.setAttribute("value",json[i][j][1])

        input.addEventListener("click",(e)=>{
          setTimeout(() => {none(e)}, 500);
        })

        d.appendChild(input)
        d.appendChild(document.createTextNode(json[i][j][0]))
        answer.appendChild(d)
        quest.appendChild(answer)
      }
      if (t){
        quest.classList.add("null")
      }
      quiz.appendChild(quest)
      t = true
      count++;
    }
  }
  let result = document.createElement("div")
  result.classList.add("null")
  result.classList.add("result")
  result.appendChild(document.createTextNode("Aguarde"))

  quest.appendChild(result)
}

fetch("./quests.json")
  .then(response => {
    return response.json();
  })
  .then(data => addQuestsJson(data));


  
