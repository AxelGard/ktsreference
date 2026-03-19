

# takeLastWhile

Returns a subsequence of this char sequence containing last characters that satisfy the given predicate.

```kotlin
inline fun CharSequence.takeLastWhile(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
fun main() {
    val text = "abc123def456"
    val lastDigits = text.takeLastWhile { it.isDigit() }
    println(lastDigits)  // prints "456"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/take-last-while.html)

    