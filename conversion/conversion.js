

const buttonC = document.querySelector(".convert_c");

const buttonF = document.querySelector(".convert_f");





buttonC.addEventListener("click", function(){
    const userInputC = document.querySelector("#c_number").value;
    let answer_c = ((userInputC - 32) * (5/9))
    const fixedValueC = answer_c.toFixed(2);
    document.querySelector(".conversion_c").textContent = fixedValueC;

})

buttonF.addEventListener("click", function(){
    const userInputF = document.querySelector("#f_number").value;
    let answer_f = ((userInputF * (5/9)) + 32)
    const fixedValueF = answer_f.toFixed(2);
    document.querySelector(".conversion_f").textContent = fixedValueF;

});