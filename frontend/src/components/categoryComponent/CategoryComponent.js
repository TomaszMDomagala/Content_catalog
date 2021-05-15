import { useState, useEffect } from 'react';

import Categories from './categories/Categories'

const CategoryComponent = () => {

    const [categories, setCategory] = useState([])

    useEffect(() => {
        const getCategory = async () => {
            const categoriesFromServer = await fetchCategory()
            setCategory(categoriesFromServer)
        }
    
        getCategory()
    }, [])

    const fetchCategory = async () => {
        const res = await fetch('http://localhost:8000/api/categoryinstances/')
        const data = await res.json()
        return data
    } 

    return (
        <div>
            <Categories categories={categories}/>
        </div>
    )
}

export default CategoryComponent
