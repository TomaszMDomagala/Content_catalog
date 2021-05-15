import { AiFillStar } from 'react-icons/ai';

import './CategoryItem.css';

const CategoryItem = ({ category }) => {

    const stars = []

    const rating = (rate) => {
        for (let i = 0; i < rate; i++) {
            stars.push(<AiFillStar key={i}/>)
        }
    }

    return (
        <div className="catgoryitem">
            <img 
            src={category.category.image} 
            alt={category.category.title}
            style={{width: 300, height: 300}}
             />
            <h3>{category.category.title}</h3>
            {category.category.author.pseudonym != null ? (
                <p className="muted">{category.category.author.pseudonym}</p>
              ) : (
                <p className="muted">
                    {category.category.author.first_name}
                    {' '}
                    {category.category.author.last_name}
                </p>
              )}
            {rating(category.rating)}
            {stars} {' ('} {category.rating} {')'}
        </div>
    )
}

export default CategoryItem
