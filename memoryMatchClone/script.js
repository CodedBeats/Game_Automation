
let selectTile = (id) => {
    
    return tile
}

let checkMatch = (t1, t2) => {
    if (t1.style.backgroundColor == t2.style.backgroundColor) {
        console.log(`Matched ${t1.id} and ${t2.id}`)
    }
}

let picked = 0
let pairs = []
let revealTile = (id) => {
    if (picked > 0) {
        pairs[1] = document.getElementById(id)
        pairs[1].style.display = "none"
        // check if pair matches when 2 have been set
        checkMatch(pairs[0], pairs[1])
        // set picked to 0 indicating to make a new pair
        picked = 0
    } else {
        // set 2nd arr val to null so a new match can be created
        pairs[1] = null
        pairs[0] = document.getElementById(id)
        pairs[0].style.display = "none"
        // set picked to 1 so the 2nd val in pairs can be filled
        picked += 1
    }
    
    console.log(pairs)
    
}

/*
        Chnage reavealTile to take 2 params
        add an ID to each div
        select those divs in different variables
        pass the divs to check match
        
*/
