
let checkMatch = (t1, t2) => {
    let matches = false
    if (t1.style.backgroundColor == t2.style.backgroundColor) {
        matches = true
    }
    return matches
}

let restartGame = () => {
    const unknowTileImgs = document.querySelectorAll("img")
    unknowTileImgs.forEach((img) => {
        img.style.display = "block"
    });
}

let picked = 0
let score = 0
let pairs = []
let tileImgs = []
let revealTile = (imgID, tileID) => {
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
            score += 1
            if (score == 4) {
                document.getElementById("won").style.display = "block"
                document.getElementById("restart").style.display = "block"
            }
        } else {
            console.log("These tiles didn't match")
            setTimeout(function() {
                console.log('3s wait before reset')
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
