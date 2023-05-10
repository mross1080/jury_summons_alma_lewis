var visitorId = ""
var lang = "en"

function initFingerprintJS() {
    FingerprintJS.load().then(fp => {
      fp.get().then(result => {
        // This is the visitor identifier:
        visitorId = result.visitorId;
        console.log(visitorId);
        retrieveUserData()
      });
    });
  }

function retrieveUserData() {
  fetch(`/retrieveUser?fingerprintId=${visitorId}`)
.then(
  function(response) {
    if (response.status !== 200) {
      console.log('Looks like there was a problem. Status Code: ' +
        response.status);
      return;
    }

    // Examine the text in the response
    response.json().then(function(data) {
        console.log("Look at this data!")
        let userData = (JSON.parse(data.name))
      console.log(JSON.parse(data.name));
      if (userData == null) {
        $(".esContent").hide()
        $(".enContent").hide()

        $(".questionContainer").append("<p>Please register to be a civilian reviewer in the first station before accessing this question</p><br>")
        $(".questionContainer").append("<p> Regístrese para ser un evaluador civil en la primera esatción antes de acceder a esta pregunta</p>")

        $(".questionContainer").css("margin-top","250px")
        $(".submitAnswerButton").hide()
        $(".lang").hide()
      } else {



      if (userData.lang === "en") {
        if (document.title == "print") {
          document.getElementById("nameEN").textContent = userData.userName
        }
        $(".esContent").hide()
        $("#langEn").css("border-bottom","3px solid white")

      } else {
        lang = "es"
        if (document.title == "print") {
          document.getElementById("nameES").textContent = userData.userName
        }
        $(".enContent").hide()
        $("#langEs").css("border-bottom","3px solid white")

      }

      // $("#ex2").modal({
      //   fadeDuration: 500
      // });
      // document.getElementById("nameEN").innerText = ` ${userData.userName}`
      // document.getElementById("nameES").innerText = ` ${userData.userName}`
    }

   
      // setTimeout(function() { $(".blocker").click()}, 3000)





    });
  }
)
.catch(function(err) {
  console.log('Fetch Error :-S', err);
});

}
const log = console.log;
const areaSelect = document.querySelector(`[id="nationalitySelect"]`);

areaSelect.addEventListener(`change`, (e) => {
  // log(`e.target`, e.target);
  const select = e.target;
  const value = select.value;
  const desc = select.options[select.selectedIndex].text;
  console.log("value ", value)
  console.log(`option desc`, desc);
});




  function submitAnswer(stationName) {
    var answer = ""

    if (stationName == "print") {
      answer = "ready"
    } else if (stationName=="selectcountry") {

      answer = document.getElementById("nationalitySelect").value
      console.log("Country ",answer)

    } else if (stationName == "stationtwo") {
      answer = $('#nationalitySelect').val().join(",")
      console.log("Names", answer)

    } else if (stationName == "banner") {
      line1 = document.getElementById("line1").value
      line2 = document.getElementById("line2").value
      line3 = document.getElementById("line3").value

      answer = `${line1},${line2},${line3}`
      console.log("Names", answer)
    } else {
      answer = document.forms[`answerForm${lang}`].elements["answerOption"].value
    }



    // var answer = document.getElementById("answer").value
    console.log(`sending answer ${answer} to /${stationName}?fingerprintId=${visitorId}&answer=${answer}`)
    fetch(`/${stationName}answer?fingerprintId=${visitorId}&answer=${answer}`)
    .then(
      function(response) {
        if (response.status !== 200) {
          console.log('Looks like there was a problem. Status Code: ' +
            response.status);
          return;
        }
    
        // Examine the text in the response
        response.json().then(function(data) {
            console.log("Look at this data!")
          console.log(data);
          $("#ex1").modal({
            fadeDuration: 300
          });

    

          document.getElementById("nextStationLink").click()
    
        //   setTimeout(function() {
        //     conso  
        //     $(".blocker").click()}, 3000)

        });
      }
    )
    .catch(function(err) {
      console.log('Fetch Error :-S', err);
    });

    

  }


function getNewVal() {

}
