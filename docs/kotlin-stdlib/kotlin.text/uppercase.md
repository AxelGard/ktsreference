

# uppercase

Converts this character to upper case using Unicode mapping rules of the invariant locale.

```kotlin
expect fun Char.uppercase(): String(source)
```

```kotlin
fun main() {
    val lower: Char = 'g'
    val upperCaseString = lower.uppercase()
    println(upperCaseString)  // prints "G"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/uppercase.html)

    