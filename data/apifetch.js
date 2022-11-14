


// fetch('url').then((response)=>{
//     return response.json()
// }).then((data)=>{
//     console.log(data)

// })

// let params={
//     method:"post",
//     headers:{
//         'Content-Type': 'application/json'
//    },
//    body:JSON.stringify(data)
// }


// }
// (/api/trip),{
//     method:'POST',
//     boyd: JSON.stringify(url),
//     headers:{
//         'Content-Type': 'application/json'
//     },

// }

// .then{(response)=> response.json()}
// .then(responseData=>{
// api url
const api_url = 
"https://www.avis.com/webapi/locations/suggestions/mesa/en_US"
  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);

    /*
        extract suggdiscription 
        place it in list
    */
    if (response) {
        hideloader();
    }
    car_reservation(list1);
}
// Calling that async function
getapi(api_url);
  
// Function to hide the loader
function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table

