$(document).ready(function() {
    $("#btn_click").on("click", function() {
      $("#hidden-container").css("opacity", 1);
  
      $("#record-button").on("click", function() {
        let elem = $(this);
  
        if (elem.hasClass('active')) {
          elem.removeClass('active');
          elem.css('background', '#4caf50');
        } else {
          elem.addClass('active');
          elem.css('background', '#ff6b6b');
        }

        var appInput = document.getElementById('app');
        
        $.post('/record', function(data) {
          let question = data.text;
          appInput.value = question;
          elem.removeClass('active');
  
          $(".btn-info").addClass("btn_active");
  
          $.ajax({
            url: '/answer',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ question: question }),
            success: function(response) {
              appInput.value = response.text;
              $.post('/speaker', function(data) {});
              elem.removeClass('active');
              $(".btn-info").removeClass("btn_active");
              $(".btn-info").addClass("btn_deactive");
  
              elem.css('background', '#4caf50');
            }
          });
        });
      });
    });

    document.addEventListener('DOMContentLoaded', () => {
        const image = document.querySelector('.dynamic-image');
    });

    $("#btn_click").on("click", function(){
      $(".btn-h1 span").addClass("btn_ghost").delay(1000).queue(function(){
        $(".btn-line").addClass("btn_gone");
        $(".btn-author").addClass("btn_gone");
        $(".btn-copy").addClass("btn_gone");
        $(".btn-button").addClass("btn_gone").delay(500).queue(function(){
          $(".btn-info").addClass("btn_white");
          $("#hidden-container").css("opacity", 1);
        });
      });
    });
});

const selected_button = document.querySelectorAll('.sidebar button');
  selected_button.forEach(button => {
  button.addEventListener('click', function() {
    selected_button.forEach(btn => btn.classList.remove('active'));
    this.classList.add('active');
    const buttonText = this.innerText;
    fetch('/api/select-model', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ button_text: buttonText })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  });
});

const buttons = document.querySelectorAll('.sidebar2 button');
  buttons.forEach(button => {
    button.addEventListener('click', function() {
      buttons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      const buttonText = this.innerText;
      fetch('/api/select-lang', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ button_text: buttonText })
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
    });
});

document.getElementById('submitBtn').addEventListener('click', function() {
  const fs = parseFloat(document.getElementById('fs').value) || 44100;
  const chunk_size = parseFloat(document.getElementById('chunk_size').value) || 1024;
  const silence_threshold = parseFloat(document.getElementById('silence_threshold').value) || 0.0001;
  const silence_duration = parseFloat(document.getElementById('silence_duration').value) || 2.5;
  const model_name = document.getElementById('model_name').value;
  const data = {
    fs: fs,
    chunk_size: chunk_size,
    silence_threshold: silence_threshold,
    silence_duration: silence_duration,
    model_name: model_name
  };

  fetch('/api/submit-data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
});

document.getElementById('prompt').addEventListener('click', function() {
  const newPrompt = document.getElementById('prompt');
  newPrompt.value = " ";
});

document.getElementById('submitBtn2').addEventListener('click', function() {
  const newPrompt = document.getElementById('prompt');

  const data = {
    prompt: newPrompt.value
  };

  newPrompt.value = "the role assigned";

fetch('/api/submit-prompt', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
});

document.getElementById('submitBtn3').addEventListener('click', function() {
  const newPrompt = document.getElementById('prompt');
  
  const data = {
    prompt: newPrompt.value
  };
  
  newPrompt.value = "the role reset";

  fetch('/api/reset-prompt', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
});

var appInput = document.getElementById('app');

appInput.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    question = appInput.value;
    appInput.value = "I answer your question right away ⚡️";

    $.ajax({
      url: '/answer',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ question: question }),
      success: function(response) {
        appInput.value = response.text;
        $.post('/speaker', function(data) {});
      }
    });
  }
});
