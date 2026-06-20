import {useState} from "react";
import API from "../api/api";


function Reverse(){

const [event,setEvent]=useState("");


const reverse = async()=>{


console.log("Sending:",event);


try{

const response = await API.post(
"/reverse/",
{
event_id:event.trim()
}
);


alert(JSON.stringify(response.data));


}
catch(error){

console.log(error.response);

alert(JSON.stringify(error.response.data));

}


}


return(

<div>

<h2>
Reverse Event
</h2>


<input

placeholder="Enter Event ID"

value={event}

onChange={
e=>setEvent(e.target.value)
}

/>


<button onClick={reverse}>
Reverse
</button>


</div>


)


}


export default Reverse;