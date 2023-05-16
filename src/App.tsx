import { useState } from 'react'
import { useReward } from 'react-rewards';

function App() {

  const [rewardInt, setReward] = useState<number>(69)
  const [text, setText] = useState(['Is YOUR cookie a winner?', '🪄'])
  const {reward: confettiReward} = useReward('confettiReward', 'confetti');
  const colors = ['#ecbbbb', '#c4e6c2', '#bfbbec', '#eceabb', '#e7dff1', '#d5d5d5']
  const loadingDialogs = ['Detecting...', 'Scanning...', 'Processing...']

  const handleClick = () => {

    if (rewardInt != 4) {
      setReward(4)
      setText(['Is YOUR cookie a winner?', '🪄'])
      return
    }

    setReward(-1)
    for (let i = 0; i < loadingDialogs.length; i++) {
      setTimeout(function() { 
        setText([loadingDialogs[i], '🔍'])
      }, 1000 * i)
    }

    setTimeout(function() {
      let num = Math.floor(Math.random() * 100);

      if (num < 45) {
        setReward(0)
        setText(['Sorry! You didn\'t win anything. Better luck next time!', '🦆'])
      } else if (45 <= num && num < 75) {
        setReward(1)
        setText(['Congrats! You won one free cookie!', '🍪'])
        confettiReward();
      } else if (75 <= num && num < 85) {
        setReward(2)
        setText(['Congrats! You won a free gaming pass!', '🎮'])
        confettiReward();
      } else {
        setReward(3)
        setText(['Congrats! You won 3 free cookies!', '🍪🍪🍪'])
        confettiReward();
        confettiReward();
        confettiReward();
        confettiReward();
      }
    }, 3000);
  }

  return (
    <>
    <div onClick={() => {
      handleClick();
    }} style={{backgroundColor: colors[rewardInt]}}>
      <h3 style={{marginBottom: '8rem'}}>Is YOUR cookie a lucky one? CookiesGPT<br/>Buy one over there! 👉</h3>
      <span id='confettiReward'></span>
      <p>{text[0]}</p>
      <p>{text[1]}</p>
    </div>
    </>
  )
}

export default App
