import CategoryItem from '../categoryItem/CategoryItem';
import './Categories.css'

const Categories = ({ categories }) => {

    return (
        <div className="items">
            {categories.map((category, index) => (
                <CategoryItem key={index} category={category} />
            ))}
        </div>
    )
}

export default Categories
