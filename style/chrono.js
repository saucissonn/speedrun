window.addEventListener("DOMContentLoaded", () => {
    const MAX_SPLITS = 48;
  
    const chrono = document.createElement("div");
    chrono.id = "chrono";
    chrono.textContent = "⏱️ 00:00:00";
    chrono.style.display = "none";
    document.body.appendChild(chrono);
  
    const button = document.createElement("button");
    button.id = "chrono-start-btn";
    button.textContent = "▶️ Chrono";
    document.body.appendChild(button);
  
    const splitBox = document.createElement("div");
    splitBox.id = "split-box";
    splitBox.style.display = "none";
    document.body.appendChild(splitBox);
  
    let startTime2;
    let intervalID;
    let splitCount2 = 0;
    let lastSplitTime = 0;
    let lastSplitStart = 0;
    let fin = false;
    let timerStarted = false;
  
    const formatTime = (ms) => {
      let totalSec = Math.floor(ms / 1000);
      let hrs = Math.floor(totalSec / 3600);
      let min = Math.floor((totalSec % 3600) / 60);
      let sec = totalSec % 60;
      return `${hrs.toString().padStart(2, '0')}:${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
    };
  
    function startTimer() {
      startTime2 = Date.now();
      chrono.style.display = "block";
      button.style.display = "none";
      intervalID = setInterval(() => {
        if (!fin) {
          const now = Date.now();
          const elapsedTime = now - startTime2;
          chrono.textContent = `⏱️ ${formatTime(elapsedTime)}`;
        }
      }, 100);
    }
  
    // Clique sur le bouton
    button.addEventListener("click", () => {
      if (!timerStarted) {
        timerStarted = true;
        startTimer();
        const now = Date.now();
        lastSplitTime = now;
        lastSplitStart = now;
      }
    });
  
    // Appui sur F4
    document.addEventListener("keydown", (e) => {
      if (e.code === "F4") {
        const now = Date.now();
  
        if (!timerStarted) {
          timerStarted = true;
          startTimer();
          lastSplitTime = now;
          lastSplitStart = now;
          return;
        }
  
        if (fin) return;
  
        if (now - lastSplitTime >= 0) {
          if (splitCount2 === 0) {
            splitBox.style.display = "block";
          }
  
          const subjectTime = (splitCount2 > 0)
            ? now - lastSplitStart
            : now - startTime2;
  
          splitCount2 += 1;
          lastSplitTime = now;
          lastSplitStart = now;
  
          const line = document.createElement("div");
          line.textContent = `Sujet ${splitCount2.toString().padStart(2, '0')} — ${formatTime(subjectTime)}`;
          splitBox.appendChild(line);
  
          if (splitCount2 >= MAX_SPLITS) {
            fin = true;
            clearInterval(intervalID);
            chrono.textContent = `⏱️ ${formatTime(now - startTime2)}`;
          }
        }
      }
    });
  });
  