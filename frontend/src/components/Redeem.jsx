import {useState} from "react";
import API from "../api/api";


function Redeem(){

const [user,setUser]=useState("");
const [points,setPoints]=useState("");



const redeem = async()=>{

try{

const response = await API.post(
"/redeem/",
{
user_id:user,
points:Number(points)
}
);


alert(JSON.stringify(response.data));


}catch(error){

alert(
JSON.stringify(error.response.data)
);

}


}



return(

<div>

<h2>
Redeem Points
</h2>


<input
placeholder="User ID"
onChange={
e=>setUser(e.target.value)
}
/>


<input
placeholder="Points"
type="number"
onChange={
e=>setPoints(e.target.value)
}
/>


<button onClick={redeem}>
Redeem
</button>


</div>

)

}


export default Redeem;