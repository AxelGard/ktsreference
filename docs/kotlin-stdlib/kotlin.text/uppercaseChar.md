

# uppercaseChar

Converts this character to upper case using Unicode mapping rules of the invariant locale.

```kotlin
expect fun Char.uppercaseChar(): Char(source)
```

```kotlin
fun main() {
    val lower = 'k'
    val upper = lower.uppercaseChar()
    println("Lower: $lower, Upper: $upper") // Output: Lower: k, Upper: K
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/uppercase-char.html)

    