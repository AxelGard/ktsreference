

# isLowerCase

Returns true if this character is lower case.

```kotlin
expect fun Char.isLowerCase(): Boolean(source)
```

```kotlin
fun main() {
    val char1: Char = 'a'
    val char2: Char = 'Z'
    println("$char1 is lower case: ${char1.isLowerCase()}") // true
    println("$char2 is lower case: ${char2.isLowerCase()}") // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-lower-case.html)

    