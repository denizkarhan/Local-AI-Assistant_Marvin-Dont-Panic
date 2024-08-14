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
  
        $.post('/record', function(data) {
          let question = data.text;
          $("#app").text(question);
          elem.removeClass('active');
  
          $(".btn-info").addClass("btn_active");
  
          $.ajax({
            url: '/answer',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ question: question }),
            success: function(response) {
              $("#app").text(response.text);
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