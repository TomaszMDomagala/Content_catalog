import StockItem from '../stockItem/StockItem';

const Stocks = ({stocks, onDelete}) => {
    return (
        <div>
            {stocks.map((stock) => (
                <StockItem key={stock.id} stock={stock} onDelete={onDelete} />
            ))}
        </div>
    )
}

export default Stocks
