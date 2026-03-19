

# singleOrNull

Returns single character, or null if the char sequence is empty or has more than one character.

```kotlin
fun CharSequence.singleOrNull(): Char?(source)
```

```kotlin
fun main() {
    val singleChar: CharSequence = "A"
    val empty: CharSequence = ""
    val multipleChars: CharSequence = "AB"

    println(singleChar.singleOrNull())     // prints: A
    println(empty.singleOrNull())          // prints: null
    println(multipleChars.singleOrNull())  // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/single-or-null.html)

    