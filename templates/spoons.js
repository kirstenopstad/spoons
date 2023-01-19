// TODO: Add spoons counter that decreases with activities added -->
document.addEventListener("DOMContentLoaded", function(){

    // Initialize spoon count
    let spoonCount = getElementById(spoon-count);
    document.querySelector("#spoon-count").innerHTML = spoonCount;

    // Define activities based on class name
    let activities = document.querySelectorAll(".activity");

    // Define reset
    let reset = document.getElementById("reset");

        // When activity is clicked

        // For # of activities
        for (let i = 0; i < activities.length; i++){

            // Deduct spoons based on activity clicked
            activities[i].addEventListener("click", function(){
                activities[i].style.backgroundColor = "green";
                spoonCount -= parseInt(activities[i].id);
                document.querySelector('#spoon-count').innerHTML = spoonCount;
            })

        // If reset is clicked, restore 15
        reset.addEventListener("click", function(){
            reset.style.backgroundColor = "green";
        })
    }
}
    // Else, disable activities and allow reset
    else {

        // If reset is clicked, restore 15
        reset.addEventListener("click", function(){
            reset.style.backgroundColor = "green";
            spoonCount = 15;
            document.querySelector('#spoon-count').innerHTML = spoonCount;
            })
        }

})