

# equals

Returns true if this character is equal to the other character, optionally ignoring character case.

```kotlin
fun Char.equals(other: Char, ignoreCase: Boolean = false): Boolean(source)
```

```kotlin
fun main() {
    val c1: Char = 'K'
    val c2: Char = 'k'

    println(c1.equals(c2, ignoreCase = true))   // true
    println(c1.equals(c2, ignoreCase = false))  // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/equals.html)

    