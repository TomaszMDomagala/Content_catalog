import { useState, useEffect } from 'react';

import Stocks from './stocks/Stocks';

const StockComponent = () => {

    const [stocks, setStocks] = useState([])

    useEffect(() => {
        const getStocks = async () => {
        const stocksFromServer = await fetchStocks()
        setStocks(stocksFromServer)
    }

    getStocks() 
    }, []) 

    const fetchStocks = async () => {
        const res = await fetch('http://127.0.0.1:8000/api/stocks/')
        const data = await res.json()
        return data
    } 

    const deleteStock = (id) => {
        setStocks(stocks.filter((stock) =>  stock.id !== id))
    }

    return (
        <div>
            <Stocks stocks={stocks} onDelete={deleteStock} />
        </div>
    )
}

export default StockComponent
