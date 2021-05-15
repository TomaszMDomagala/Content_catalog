import './Button.css'

const Button = ({ name, startTimer }) => {
    return (
        <div>
            <button id="button" type="button" onClick={startTimer}>{ name }</button>
        </div>
    )
}

export default Button
