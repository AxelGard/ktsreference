

# asArray

Converts the result of RegExp.exec to an array where the first element contains the entire matched text and each subsequent element is the text matched by each capturing parenthesis.

```kotlin
inline fun RegExpMatch.asArray(): Array<out String?>(source)
```

```kotlin
import kotlin.js.RegExp

fun main() {
    val regex = RegExp("(\\w+)\\s(\\w+)")
    val text   = "Hello world"

    val match = regex.exec(text)           // RegExpMatch?
    val parts = match?.asArray()           // Array<out String?>

    println(parts?.joinToString(separator = ", "))  // prints: Hello world, Hello, world
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/as-array.html)

    