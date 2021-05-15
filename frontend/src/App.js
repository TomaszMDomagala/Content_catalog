import { BrowserRouter as Router, Route } from 'react-router-dom'; 

import Header from './components/header/Header';
import StockComponent from './components/stockComponent/StockComponent';
import CategoryComponent from './components/categoryComponent/CategoryComponent';
import TimerComponent from './components/timerComponent/TimerComponent';

const App = () => {
  return (
    <Router>
      <div className="container">
        <Route path="/stocks" exact render={(props) => (
          <>
            <div className="container">
              <Header title='Stocks' />
              <StockComponent />
            </div>
          </>
        )} />
        <Route path="/categories" exact render={(props) => (
          <>
            <div className="container">
              <Header title='Media' />
              <CategoryComponent />
            </div>
          </>
        )} />
        <Route path="/timer" exact render={(props) => (
          <>
            <div className="timer">
              <Header title='Timer' />
              <TimerComponent />
            </div>
          </>
        )} />
      </div>
    </Router>
  );
}

export default App;
