

# takeWhile

Returns a subsequence of this char sequence containing the first characters that satisfy the given predicate.

```kotlin
inline fun CharSequence.takeWhile(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
fun main() {
    val str = "abc123xyz"
    val letters = str.takeWhile { it.isLetter() }
    println(letters)  // prints: abc
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/take-while.html)

    