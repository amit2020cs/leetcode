/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function(times) {
    if (times === 0) {
        return "";
    }
    //Here "this" refers to the string object on which the method is called
    return this + this.replicate(times - 1);
}