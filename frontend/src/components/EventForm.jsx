import {useState} from "react";
import API from "../api/api";


function EventForm(){


const [data,setData]=useState({

event_id:"",
user_id:"",
event_type:"deposit",
amount:100,
timestamp:"2026-06-20"

});



const submit=async()=>{


let response = await API.post(
"/events/",
data
);


alert(JSON.stringify(response.data));


}



return (

<div>

<h2>Add Event</h2>


<input
placeholder="Event ID"
onChange={
e=>setData({
...data,
event_id:e.target.value
})
}
/>


<input
placeholder="User ID"
onChange={
e=>setData({
...data,
user_id:e.target.value
})
}
/>


<input
type="number"
min="1"
placeholder="Amount"
onChange={
e=>setData({
...data,
amount:e.target.value
})
}
/>


<button onClick={submit}>
Submit Event
</button>


</div>

)

}


export default EventForm;
