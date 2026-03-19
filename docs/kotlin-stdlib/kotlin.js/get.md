

# get

Returns the entire text matched by RegExp.exec if the index parameter is 0, or the text matched by the capturing parenthesis at the given index.

```kotlin
inline operator fun RegExpMatch.get(index: Int): String?(source)
```

```kotlin
import kotlin.js.RegExp

fun main() {
    val regex = RegExp("(\\w+)\\s(\\d+)")
    val match = regex.exec("hello 42")   // RegExpMatch?

    if (match != null) {
        println("Full match: ${match[0]}")   // index 0
        println("Word part: ${match[1]}")    // capturing group 1
        println("Number part: ${match[2]}")  // capturing group 2
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/get.html)

    