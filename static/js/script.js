$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
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
    /* Add Ingredient */
    const addNewIngredient = () => {
        let i;
        $('#add_ingredient').click(()=> {
            i++;
            $('#ingredients_list').append('<input name="ingredients_list" id="ingredients_list" minlength="5"  type="text" value="{{ ingredient }}" class="validate"')
        })
    }
    addNewIngredient();

    const addMethod = () => {
        let i;
        $('#add_method').click(()=> {
            i++;
            $('#method_list').append('<input id="recipe_method" name="recipe_method[]" minlength="5" class="validate" required>')
        })
    }
    addMethod();

    const addTool = () => {
        let i;
        $('#add_tool').click(()=> {
            i++;
            $('#tool_list').append('<input id="recipe_tools" name="recipe_tools[]" minlength="5" class="validate">')
        })
    }
    addTool();
    
});