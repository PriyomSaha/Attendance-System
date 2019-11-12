$(document).ready(function(){
  // canvas.height = window.innerHeight;
  // canvas.width = window.innerWidth;
 var diagram = [];
  $(".div").draggable({
      helper: "clone",
      cursor:"move"
  });
  $(".canvas").droppable({
    accept: ".div" ,
    drop : function(event, ui){
      var node = {
        id : (new Date).getTime(),
        position : ui.position
      };
      if(ui.helper.hasClass("div1"))
      {
        node.type = "Mark present";
      }
      else if (ui.helper.hasClass("div2"))
      {
        node.type = "Mark absent";
      }
      else if(ui.helper.hasClass("div3"))
      {
        node.type = "Call Student";
      }
      else if (ui.helper.hasClass("div4"))
      {
        node.type = "Send Notification to Student";
      }
      else if(ui.helper.hasClass("div5"))
      {
        node.type = "Parents Call";
      }
      else if (ui.helper.hasClass("div6"))
      {
        node.type = "Send Notification to Parents";
      }
      diagram.push(node);
      var top = node.position.top;
      var left = node.position.left
      console.log(top,left);
      $(this).append($(ui.draggable).clone().removeClass("div").addClass("custom").resizable());
      $(".custom").draggable();
    }
  });
});
