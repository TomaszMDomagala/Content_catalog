import { FaTimes } from 'react-icons/fa'; 
import { useState, useEffect } from 'react';

import './StockItem.css'

const StockItem = ({stock, onDelete}) => {

    let whatIPaid;
    let percentage;
    let actualPrice;

    const [apistock, setStock] = useState([])

    useEffect(() => {
        const getStock = async () => {
            const stockFromApi = await fetchStock()
            setStock(stockFromApi)
        }

        getStock()
    }) 

    const fetchStock = async () => {
        const res = await fetch(`https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?symbol=${stock.stock_name}&region=US`, {
            "method": "GET",
            "headers": {
                "x-rapidapi-key": "c64558b2afmsh264b97a956719cep15dcd7jsn165b9a1f32fa",
                "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
        })
        const data = await res.json()
        return data
    }

    if (apistock.length !== 0) {
        actualPrice = Math.round(((stock.amount * apistock.price.regularMarketPrice.fmt) + Number.EPSILON) * 100) / 100;
        whatIPaid = Math.round(((stock.amount * stock.value_at_buy) + Number.EPSILON) * 100) / 100;
        percentage = (((actualPrice - whatIPaid)/whatIPaid) * 100).toFixed(2);
    }

    return (
        <div className={`stock ${whatIPaid < actualPrice ? 'profit' : 'loss'}`}>
            <h3> {stock.name} <FaTimes style={{ color: 'red', cursor: 'pointer '}} onClick={() => onDelete(stock.id)} /></h3>
            <p> {actualPrice} {'$'}  {percentage} {'%'} </p>
        </div>
    )
}

export default StockItem
