$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    
    
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

    // I is declared outside the add function
    let i=0

    /* Add Ingredient */
    const addNewIngredient = () => {
        // let i;
        $('#add_ingredient').click(()=> {
            i++;
            // Use backticks so that you can insert i inside
            $('#ingredients_list').append(`<input type="text" id="recipe_ingredients_${i}" name="recipe_ingredients[${i}]" minlength="5" class="validate" placeholder="ingredients" required>`)
        })
    }
    addNewIngredient();

    /* Delete Ingredient */
    const delIngredient = () => {
        $('#del_ingredient').click(()=> {
            $(`#recipe_ingredients_${i}`).remove()
            i--;
        })
        console.log(i)
    }
    delIngredient();

    const addMethod = () => {
        let i;
        $('#add_method').click(()=> {
            i++;
            $('#method_list').append('<input id="recipe_method" name="recipe_method[]" minlength="5" class="validate" placeholder="cooking method" required>')
        })
    }
    addMethod();

    const addTool = () => {
        let i;
        $('#add_tool').click(()=> {
            i++;
            $('#tool_list').append('<input id="recipe_tools" name="recipe_tools[]" minlength="5" class="validate" placeholder="cooking tools">')
        })
    }
    addTool();
    
});