import API from "../api/api";


function Reverse(){


const reverse=async()=>{


let res = await API.post(
"/reverse/",
{
event_id:"EV001"
}
);


alert(JSON.stringify(res.data));


}


return (

<div>

<h2>Reverse</h2>

<button onClick={reverse}>
Reverse Event
</button>


</div>

)

}


export default Reverse;