import { useState, useEffect } from "react"
import api from "src/utils/api"
import Maps from "src/components/Maps"

const Home = () => {
    const [rentals, setRentals] = useState([])

    useEffect(() => {
        const caller = async () => {
            const res = await api.get('room/')
            console.log(res.data)
            setRentals(res.data)
        }
        caller()
    }, [])

    return (
        <div>
            <h1>This is Home!</h1>
            <h1>!!notes!! dapat andito yung maps tas parang cards nung mga Avaiable na rental homes</h1>

            <section>
                <Maps />
            </section>


            {/* dapat card yung mga rentals */}
            {rentals.map((rental) => (
                <div key={rental.room_id}>
                    <img src={rental.room_picture} alt={rental.name}/>
                    <h1>Room name: {rental.name}</h1>
                    <p>address: {rental.address}</p>
                    <p>Airconditioned: {rental.air_condition ? "It has aircon" :"it does not have aircon"}</p>
                    <p>Comfortroom: {rental.comfort_room ? "it has cr": "no cr"}</p>
                    <p>Internet: {rental.internet ? "yes internet" : "no internet"}</p>
                    <p>Avaiable: {rental.room_availability}</p>
                    <p>Price: {rental.price}</p>
                    <button>rent now</button>
                </div>
            ))}

        </div>
    )
}

export default Home