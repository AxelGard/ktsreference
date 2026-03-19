

# reset

Resets the regular expression so that subsequent RegExp.test and RegExp.exec calls will match starting with the beginning of the input string.

```kotlin
fun RegExp.reset()(source)
```

```kotlin
import kotlin.js.RegExp
import kotlin.js.RegExpExecArray

fun main() {
    val regex = RegExp("a", "g")
    val text = "abacadae"

    var match: RegExpExecArray? = regex.exec(text)
    while (match != null) {
        println("Found 'a' at index ${match.index}")
        match = regex.exec(text)
    }

    regex.reset()

    match = regex.exec(text)
    while (match != null) {
        println("Found 'a' at index ${match.index} after reset")
        match = regex.exec(text)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/reset.html)

    