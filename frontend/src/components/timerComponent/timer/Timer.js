import Button from './button/Button';
import './Timer.css'

const Timer = () => {

    let hr = 0;
    let min = 0;
    let sec = 0;
    let time = '00:00:00';
    let stoptime = true;

    function startTimer() {
        if (stoptime === true) {
            stoptime = false;
            timerCycle();
        }
    }
    function stopTimer() {
        if (stoptime === false) {
        stoptime = true;
        }
    }
    
    function resetTimer() {
        time = '00:00:00';
        stoptime = true;
        hr = 0;
        sec = 0;
        min = 0;
    }

    function timerCycle() {
        if (stoptime === false) {
        sec = parseInt(sec);
        min = parseInt(min);
        hr = parseInt(hr);
    
        sec = sec + 1;
    
        if (sec === 60) {
            min = min + 1;
            sec = 0;
        }
        if (min === 60) {
            hr = hr + 1;
            min = 0;
            sec = 0;
        }
  
        if (sec < 10 || sec === 0) {
            sec = '0' + sec;
        }
        if (min < 10 || min === 0) {
            min = '0' + min;
        }
        if (hr < 10 || hr === 0) {
            hr = '0' + hr;
        }
  
        time = hr + ':' + min + ":" + sec;
  
        setTimeout("timerCycle()", 1000);
        }
    }   

    return (
        <div>
            <div id="stopwatch">
                {time}
            </div>
            <div className='buttons'>
            <Button name='start' onClick={startTimer} />
            </div>
        </div>
    )
}

export default Timer