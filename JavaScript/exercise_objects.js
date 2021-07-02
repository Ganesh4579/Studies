// a) Create a function to build an object which represents a cricket player.The object should have properties
// for -name, specialization, matches played, total number of runs scored, total wickets taken, 
// individual runs scored in last ten matches, individual wickets taken in last ten matches.

function getObject() {
    return {
        name: "Dhoni",
        specialization: "WicketKeeper-Batsman",
        matchesPlayed: 300,
        totalNumberOfRunsScored: 10050,
        totalWicketsTaken: 68,
        individualRunsLastTenMatches: getRunArray(),
        individualWicketsLastTenMatches: getWicketArray(),

    }
}

function getRunArray() {
    let runs = new Array(10);
    for (i = 0; i < runs.length; i++) {
        runs[i] = Math.round(Math.random() * 145);
    }
    return runs;
}


function getWicketArray() {
    let wickets = new Array(10);
    for (i = 0; i < wickets.length; i++) {
        wickets[i] = Math.abs(Math.round((Math.random() * 10) - 6));
    }
    return wickets;
}

// console.log(getObject());

// b.Create an array of 11 cricket players to represent a team.
// Bonus: You may create a loop and use a random number generator to populate the numerical values.

function playingEleven() {
    return ["Rohit",
        "KL Rahul",
        "Virat Kholi",
        "MS Dhoni",
        "Hardik Pandya",
        "Rishab Pant",
        "Ravindra Jadeja",
        "Bhuvaneshwar Kumar",
        "Mohamad Shanmi",
        "Zaheer Khan",
        "Harbajan Singh "
    ]
}

let team = playingEleven();
let player = getObject();


//2.Add a method to the object which prints the player’s average runs in the last five matches

player.averageRunsLastFiveMatches = function() {
    let avg = 0;
    for (let i = 4; i < this.individualRunsLastTenMatches.length; i++) {
        avg += this.individualRunsLastTenMatches[i];
    }
    return avg / 5;

}

// console.log(player.averageRunsLastFiveMatches());

//3. Add a method to the object which prints the player’ s average wickets taken in the last five matches


player.averageWicketsLastFiveMatches = function() {
    let avg = 0;
    for (let i = 4; i < this.individualWicketsLastTenMatches.length; i++) {
        avg += this.individualWicketsLastTenMatches[i];
    }
    return avg / this.individualWicketsLastTenMatches.length;

}

//4. Add a method to the object which prints the player’ s average runs in the last’ n’ matches where’ n’ is provided by the user


player.averageRuns = function(n) {
    let avg = 0;
    for (let i = n - 1; i < this.individualRunsLastTenMatches.length; i++) {
        avg += this.individualRunsLastTenMatches[i];
    }
    return avg / n;

}

//5. Add a method to the object which prints the player’ s average wickets taken in the last’ n’ matches where’ n’ is provided by the user
player.averageWickets = function(n) {
    let avg = 0;
    for (let i = n - 1; i < this.individualWicketsLastTenMatches.length; i++) {
        avg += this.individualWicketsLastTenMatches[i];
    }
    return avg / n;

}

// console.log(player);
// console.log(player.averageRuns(7));
// console.log(player.averageRunsLastFiveMatches());
// console.log(player.averageWickets(6));


//6. Add a method to the object which can add the score in a new match to the player’ s tally.
// What properties should be updated and how ? The method should update all the properties correctly

//7. Add a method to the object which can add the number of wickets in a new match to the player’ s tally.
// What properties should be updated and how ? The method should update all the properties correctly.
player.updateMatch = function(runs, wickets) {
    if (wickets == undefined) {
        this.updateScore(runs);
        this.updateWickets(0)
    } else {
        this.updateScore(runs);
        this.updateWickets(wickets)
    }
    this.matchesPlayed += 1;
}


player.updateScore = function(n) {
    this.totalNumberOfRunsScored += n;
    this.individualRunsLastTenMatches.splice(0, 1);
    this.individualRunsLastTenMatches.push(n);

}

player.updateWickets = function(n) {
        this.totalWicketsTaken += n;
        this.individualWicketsLastTenMatches.splice(0, 1);
        this.individualWicketsLastTenMatches.push(n);
    }
    // player.updateMatch(30)
    // console.log(player);

// 8.Add a method to the object which takes an object of the format below as the input and updates the wickets and runs as per questions 6, 7 above.
// Example object: { runs: 32, wickets: 1 }
player.updateMatchWithObj = function(obj) {
    this.updateMatch(obj.runs, obj.wickets)
}

player.updateMatchWithObj({
        runs: 40,
        wickets: 3
    })
    // console.log(player);



// 9.Add a method to the object which prints the player’ s summary details.The details needed are:
// Name,
// Specialization
// Matches played
// Total number of runs scored
// Total wickets taken
// Average runs in last ten matches
// Average wickets in last ten matches
// Overall Average runs scored

player.printPlayer = function() {
    console.log("Name \t" + this.name)
    console.log("Specialization \t" + this.specialization)
    console.log("Matches played \t" + this.matchesPlayed)
    console.log("Total number of runs scored \t" + this.totalNumberOfRunsScored)
    console.log("Total wickets taken \t" + this.totalNumberOfRunsScored)
    console.log("Average runs in last ten matches \t" + this.averageRuns(1))
    console.log("Average wickets in last ten matches \t" + this.averageWickets(1))
    console.log("Overall Average runs scored \t" + this.totalNumberOfRunsScored / this.matchesPlayed)
}

player.printPlayer();

// Bonus question: Write two functions which sort the array of players in ascending order by their runs scored and wickets
//taken respectively.The functions should add a property to the object denoting their runs rank or wickets rank.