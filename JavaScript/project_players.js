function getRunArray() { // Generate random run array for each player
    let runs = new Array(10);
    for (i = 0; i < runs.length; i++) {
        runs[i] = Math.round(Math.random() * 145);
    }
    return runs;
}

function getWicketArray() { // Generate random wicket array for each player
    let wickets = new Array(10);
    for (i = 0; i < wickets.length; i++) {
        wickets[i] = Math.abs(Math.round((Math.random() * 10) - 6));
    }
    return wickets;
}

let averageRunsLastFiveMatches = function(player) { //Generate players average runs in last Five Matches 
    let average = 0;
    for (let i = 4; i < player.runsLastTenMatches.length; i++) {
        average += player.runsLastTenMatches[i];
    }
    return average / 5;
}

let averageWicketsLastFiveMatches = function(player) { //Generate players average wickets in last Five Matches 
    let average = 0;
    for (let i = 4; i < player.wicketsLastTenMatches.length; i++) {
        average += player.wicketsLastTenMatches[i];
    }
    return average / 5;
}

let averageRuns = function(player, n) { //Generate players average runs according to user input
    let average = 0;
    for (let i = n - 1; i < player.runsLastTenMatches.length; i++) {
        average += player.runsLastTenMatches[i];
    }
    return average / n;
}


let averageWickets = function(player, n) { //Generate players average wickets according to user input
    let average = 0;
    for (let i = n - 1; i < player.wicketsLastTenMatches.length; i++) {
        average += player.wicketsLastTenMatches[i];
    }
    return average / n;
}

let updateMatch = function(player, runs, wickets) { //updating players runs and wickets along with every match
    if (wickets) {
        updateScore(player, runs);
        updateWickets(player, 0)
    } else {
        updateScore(player, runs);
        updateWickets(player, wickets)
    }
    player.matchesPlayed += 1;
}


let updateScore = function(player, score) { //updating player score
    player.totalRunsScored += score;
    player.runsLastTenMatches.splice(0, 1);
    player.runsLastTenMatches.push(score);
}

let updateWickets = function(player, wickets) { //updating players wicket
    player.totalWicketsTaken += wickets;
    player.wicketsLastTenMatches.splice(0, 1);
    player.wicketsLastTenMatches.push(wickets);

}
let updateMatchWithObject = function(player, object) { //updating players runs and wicket with user object
    updateMatch(player, object.runs, object.wickets)
}

let averageWicketsLastTenMatches = function(player) { //Generate average wicket last ten matches of a player
    let average = 0;
    for (let i = 0; i < player.wicketsLastTenMatches.length; i++) {
        average += player.wicketsLastTenMatches[i];
    }
    return average / player.wicketsLastTenMatches.length;
}

let averageRunsLastTenMatches = function(player) { //Generate average wicket last ten matches of a player
    let average = 0;
    for (let i = 0; i < player.runsLastTenMatches.length; i++) {
        average += player.runsLastTenMatches[i];
    }
    return average / player.runsLastTenMatches.length;
}

let printPlayer = function(player) { //print player profile
    console.log("Name \t" + player.name);
    console.log("Specialization \t" + player.specialization);
    console.log("Matches played \t" + player.matchesPlayed);
    console.log("Total number of runs scored \t" + player.totalRunsScored);
    console.log("Total wickets taken \t" + player.totalWicketsTaken);
    console.log("Average runs in last ten matches \t" + averageRunsLastTenMatches(player));
    console.log("Average wickets in last ten matches \t" + averageWicketsLastTenMatches(player));
    console.log("Overall Average runs scored \t" + player.totalRunsScored / player.matchesPlayed);
}

let playing11 = ["Rohit",
    "KL Rahul",
    "Virat Kholi",
    "MS Dhoni",
    "Hardik Pandya",
    "Rishab Pant",
    "Ravindra Jadeja",
    "Bhuvaneshwar Kumar",
    "Mohamad Shami",
    "Zaheer Khan",
    "Harbajan Singh "
]


let t_Wickets = [20, 10, 30, 25, 45, 75, 87, 200, 400, 800, 780]


let t_Runs = [
    15045, 13098, 12564, 10000, 1433, 1980, 1567, 2678, 1256, 890, 600
]


let mtsPlayed = [
    100, 130, 230, 300, 124, 155, 310, 120, 167, 176, 127
]


let specs = ["Batsman",
    "Batsman",
    "Batsman",
    "WicketKeeper-Batsman ",
    "All-Rounder",
    "Batsman",
    "All-Rounder",
    "Bowler",
    "Bowler",
    "Bowler",
    "Bowler"
]

function getPlayers() { //Generate array of player object
    let allPlayers = []
    for (let i = 0; i < 11; i++) {
        let temp = new Object();
        temp.name = playing11[i];
        temp.specialization = specs[i];
        temp.matchesPlayed = mtsPlayed[i];
        temp.totalRunsScored = t_Runs[i];
        temp.totalWicketsTaken = t_Wickets[i];
        temp.runsLastTenMatches = getRunArray();
        temp.wicketsLastTenMatches = getWicketArray();
        allPlayers.push(temp);
    }
    return allPlayers;
}

function playerLast5MatchRuns(player) {
    console.log(`\n ${player.name} had scored ${averageRunsLastFiveMatches(player)} average runs in last 5 matches.\n`);
}

function playerLast5MatchWickets(player) {
    console.log(`\n ${player.name} had taken ${averageWicketsLastFiveMatches(player)} average wickets in last 5 matches.\n`);
}

function playerLastMatchWickets(player, n) {
    console.log(`\n ${player.name} had taken ${averageWickets(player,n)} average wickets in last ${n} matches.\n`);
}

function playerLastMatchRuns(player, n) {
    console.log(`\n ${player.name} had scored ${averageRuns(player,n)} average runs in last ${n} matches.\n`);
}


let team = getPlayers();
//console.log(team.length);
printPlayer(team[0]); //prints single player profile
console.log("\n");
playerLast5MatchRuns(team[0]); 
playerLast5MatchWickets(team[0]);
playerLastMatchRuns(team[0], 6);
playerLastMatchWickets(team[0], 7);

for (let j of team) { // print all players profile
    console.log("\n");
    printPlayer(j);
    console.log("\n");
}
