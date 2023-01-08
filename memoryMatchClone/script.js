// set all global variables
const wonBanner = document.getElementById("won")
const restartButton = document.getElementById("restart")
const moveCounter = document.getElementById("counter")
let picked = 0
let score = 0
let moves = 0
let pairs = []
let tileImgs = []

let checkMatch = (t1, t2) => {
    let matches = false
    if (t1.style.backgroundImage == t2.style.backgroundImage) {
        matches = true
    }
    // return a bool to be assigned to a variable when calling the func
    return matches
}

let restartGame = () => {
    // hide wonBanner
    wonBanner.style.display = "none"

    // bring back all imgs
    const unknowTileImgs = document.querySelectorAll("img")
    unknowTileImgs.forEach((img) => {
        img.style.display = "block"
    });

    // reset moves made and score, remove winning text 
    moves = 0
    score = 0
    moveCounter.innerHTML = `Moves Made: ${moves}`
}

let revealTile = (imgID, tileID) => {
    moves += 1
    moveCounter.innerHTML = `Moves Made: ${moves}`

    if (picked > 0) {
        // store 2nd selected tile in arrs
        pairs[1] = document.getElementById(tileID)
        tileImgs[1] = document.getElementById(imgID)

        // hide tile image
        tileImgs[1].style.display = "none"

        // check if pair matches when 2 have been set
        let tilesMatch = checkMatch(pairs[0], pairs[1])
        if (tilesMatch) {
            console.log("These tiles matched")
            // increment score when a pair is found
            score += 1
            // check if all pairs have been found to indicate the end of the game
            if (score == 4) {
                wonBanner.style.display = "block"
                restartButton.style.display = "block"
            }
        } else {
            console.log("These tiles didn't match")
            // add delay so user can see both tiles together before reseting the images
            setTimeout(function() {
                // could use a for loop but it's just 2 lines anyway
                tileImgs[0].style.display = "block"
                tileImgs[1].style.display = "block"
            }, 1000);
            
        }

        // set picked to 0 indicating to make a new pair
        picked = 0
    } 
    else {
        // set 2nd arr vals to null so a new match can be created
        pairs[1] = null
        tileImgs[1] = null
        
        // store 1st selected tile in arrs
        pairs[0] = document.getElementById(tileID)
        tileImgs[0] = document.getElementById(imgID)

        // hide tile image
        tileImgs[0].style.display = "none"

        // set picked to 1 so the 2nd val in pairs can be filled
        picked += 1
    }
}

/*
======
    There are lots of errors that can occur
    But this small game is just designed for testing image matching programs
======
*/
