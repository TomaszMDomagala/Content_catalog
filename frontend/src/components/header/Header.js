import PropTypes from 'prop-types'; 
import { Link } from 'react-router-dom';

import './Header.css';

const Header = ({ title }) => {
    return (
        <div>
            <header className='header'>
                <h1>{title}</h1>   
                <Link to="/categories">Rate Your Media</Link>
                <Link to="/stocks">Stocks</Link >
            </header>
        </div>
    )
}

Header.defaultProps = {
    title: 'My app'
}

Header.propTypes = {
    title: PropTypes.string
}

export default Header
