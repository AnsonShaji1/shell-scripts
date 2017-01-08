var canvas,context,dragg=false,startlocation,snapshot,linew,fillcolor;

function dragStart(event){
	dragg=true;
	var shape=document.querySelector('input[type="radio"][name="shape"]:checked').value;
	if(shape =="pencil" || shape == "rubber"){
		context.beginPath();
		startlocation=canvasCoordinate(event);
		context.moveTo(startlocation.x,startlocation.y);
		}
	else{
		startlocation=canvasCoordinate(event);
		takesnapshot();
		}
	
	
	}


function drag(event){
	var p;
	if(dragg == true){
		var shape=document.querySelector('input[type="radio"][name="shape"]:checked').value;
		if(shape =="pencil" || shape =="rubber"){
			p=canvasCoordinate(event);
			draw(p);
			}
		else{
			restoresnapshot();
			p=canvasCoordinate(event);
			draw(p);
			}
		}
	}
		

function dragStop(event){
	var p;
	dragg=false;
	var shape=document.querySelector('input[type="radio"][name="shape"]:checked').value;
	if(shape =="pencil" || shape =="rubber"){
		p=canvasCoordinate(event);
		draw(p);
		}
	else{
		restoresnapshot();
		p=canvasCoordinate(event);
		draw(p);
		}
	}



function canvasCoordinate(event){
	x=event.clientX - canvas.getBoundingClientRect().left;
	y=event.clientY - canvas.getBoundingClientRect().top;
	return{x:x,y:y};
	}


function draw(position){
	var fillbox=document.getElementById("fillbox");
	var shape=document.querySelector('input[type="radio"][name="shape"]:checked').value;
	var linecap=document.querySelector('input[type="radio"][name="lineCap"]:checked').value;
	context.lineCap=linecap;
	//console.log(shape);
	//console.log(polygonside);
	
	if(shape == "line"){
		drawline(position);
		}
	if(shape == "circle"){
		drawcircle(position);	
		}
	if(shape =="poly"){
		var s,t;
		s=findside();
		t=findangle();
		drawpoly(position,s,t*(Math.PI)/180);
		}
	if(shape =="pencil"){
		drawpencil(position);
		}
	if(shape =="rubber"){
		drawrubber(position);
		}
	if(fillbox.checked){
		context.fillStyle =fillcolor.value;
		context.fill();
		}
	else{
		context.strokeStyle=fillcolor.value;
		context.stroke();
		}	
	}


function drawpencil(position){
	//context.moveTo(startlocation.x,startlocation.y);
	context.lineTo(position.x,position.y);
	context.strokeStyle=fillcolor.value;
	context.stroke();
	context.beginPath();
	context.moveTo(position.x,position.y);
	}


function drawrubber(position){
	//context.moveTo(startlocation.x,startlocation.y);
	context.lineTo(position.x,position.y);
	context.strokeStyle="white";
	context.lineWidth=30;
	context.stroke();
	context.beginPath();
	context.moveTo(position.x,position.y);
	}


function drawline(position){
	context.moveTo(startlocation.x,startlocation.y);
	context.lineTo(position.x,position.y);
	context.strokeStyle=fillcolor.value;
	context.stroke();
	context.beginPath();
	context.moveTo(position.x,position.y);
	}


function takesnapshot(){
	snapshot=context.getImageData(0,0,canvas.width,canvas.height);
	}


function restoresnapshot(){
	context.putImageData(snapshot,0,0);
	}



function drawcircle(position){
	context.beginPath();
	var radius=Math.sqrt(Math.pow((position.x - startlocation.x),2) + Math.pow((position.y - startlocation.y),2));
	context.arc(startlocation.x,startlocation.y,radius,0,2*Math.PI);
	}


function drawpoly(position,sides,angle){
	var coordinates=[];
	var radius=Math.sqrt(Math.pow((position.x - startlocation.x),2) + Math.pow((position.y - startlocation.y),2));
	var index=0;
	for(index=0;index<sides;index++){
		coordinates.push({x:startlocation.x + radius * Math.cos(angle),y:startlocation.y - radius *Math.sin(angle)});
		angle +=(2 * Math.PI)/sides;
		}
	context.beginPath();
	context.moveTo(coordinates[0].x,coordinates[0].y);
	for(index=1;index < sides;index++){
		context.lineTo(coordinates[index].x,coordinates[index].y);
		}
	context.closePath();
	
	}





function findside(){
	var polygonside=document.getElementById("polygonside");
	var slidervalue=polygonside.value;
	document.getElementById("outputside").innerHTML=slidervalue;
	return slidervalue;
	
	}

function findangle(){
	var polygonangle=document.getElementById("polygonangle");
	var anglevalue=polygonangle.value;
	document.getElementById("outputangle").innerHTML=anglevalue;
	return anglevalue;
	}

function changelinewidth(event){
	context.lineWidth=this.value;
	event.stopPropagation();
	}


function changefillcolor(event){
	context.fillStyle=this.value;
	event.stopPropagation();
	}

function changebgcolor(event){
	context.save();
	context.fillStyle=document.getElementById('bgcolor').value;
	context.fillRect(0,0,canvas.width,canvas.height);
	context.restore();
	}

function canvasclear(event){
	context.clearRect(0,0,canvas.width,canvas.height);
	}


function saveImage(){
	var data=canvas.toDataURL();
	window.open(data,'_blank','location=0 menubar=0');
	}

function init(){
	canvas=document.getElementById("a");
	context=canvas.getContext("2d");
	linew=document.getElementById("line_width");
	fillcolor=document.getElementById("fillcolor");
	var bgcolor=document.getElementById("bgcolor"),
	clearcanvas=document.getElementById("clear");
	
	context.lineWidth=linew.value;
	var saveButton=document.getElementById("save");

	//context.globalCompositeOperation = 'lighter';

	canvas.addEventListener('mousedown',dragStart,false);
	canvas.addEventListener('mousemove',drag,false);
	canvas.addEventListener('mouseup',dragStop,false);
	linew.addEventListener('input',changelinewidth,false);
	fillcolor.addEventListener('input',changefillcolor,false);
	bgcolor.addEventListener('input',changebgcolor,false);
	clearcanvas.addEventListener('click',canvasclear,false);
	saveButton.addEventListener('click',saveImage,false);
	
	}
window.addEventListener('load',init,false);

