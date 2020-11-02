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

        $(this).on("click", "#add_ingredient", function(){
            var html = '<div id="ingredients"><input name="recipe_ingredients[]" id="recipe_ingredients" minlength="5" type="text" class="validate" placeholder="ingredients"></div>';
        
            $(".ingredients").append(html);
        });

    

    
    /* Add Method */
    const addMethod = () => {
        $('#add_method').click(()=> {
            i++;
            $('#method_list').append(`<input id="recipe_method_${i}" name="recipe_method[${i}]" minlength="5" class="validate" placeholder="cooking method" required>`)
        })
    }
    addMethod();

    /* Delete Method */
    const delMethod = () => {
        $('#del_method').click(()=> {
            $(`#recipe_method_${i}`).remove()
            i--;
        })
        console.log(i)
    }
    delMethod();


    /* Add Tool */
    const addTool = () => {
        $('#add_tool').click(()=> {
            i++;
            $('#tool_list').append(`<input id="recipe_tools_${i}" name="recipe_tools[${i}]" minlength="5" class="validate" placeholder="cooking tools">`)
        })
    }
    addTool();


    /* Delete Tool */
    const delTool = () => {
        $('#del_tool').click(()=> {
            $(`#recipe_tools_${i}`).remove()
            i--;
        })
        console.log(i)
    }
    delTool();
    
});