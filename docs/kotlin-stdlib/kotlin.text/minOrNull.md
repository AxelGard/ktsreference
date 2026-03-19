

# minOrNull

Returns the smallest character or null if the char sequence is empty.

```kotlin
fun CharSequence.minOrNull(): Char?(source)
```

```kotlin
fun main() {
    val nonEmpty = "Kotlin"
    val empty = ""

    println(nonEmpty.minOrNull())  // prints 'K'
    println(empty.minOrNull())     // prints 'null'
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-or-null.html)

    