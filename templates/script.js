window.addEventListener('load', function () {
  let net;
  let isPredicting = false;
  function startPredicting(){
    isPredicting=true;
    app();
  }
  async function app(){
    console.log('Loading model..');
    net= await tf.automl.loadTextClassification('predict.py');
    console.log('Successfully loaded model');

});

async function app(){
 console.log('Loading model..');
 net= await tf.automl.loadImageClassification('model.json');
 console.log('Successfully loaded model');
 

 while(isPredicting){

 
 console.log(result);
 
 document.getElementById("predictions-mask").innerText=result['0']['label']+": "+Math.round(result['0']['prob']*100)+"%";
 document.getElementById("predictions-no-mask").innerText=result['1']['label']+": "+Math.round(result['1']['prob']*100)+"%";
img.dispose();
 
await tf.nextFrame();
 
 }
 
}
