import API from "../api/api";


function Redeem(){


const redeem=async()=>{


let res = await API.post(
"/redeem/",
{
user_id:"USER1",
points:10
}
);


alert(JSON.stringify(res.data));


}



return (

<div>

<h2>Redeem</h2>

<button onClick={redeem}>
Redeem 10 Points
</button>


</div>

)

}


export default Redeem;