

# partition

Splits the original char sequence into a pair of char sequences, where first char sequence contains characters for which predicate yielded true, while second char sequence contains characters for which predicate yielded false.

```kotlin
inline fun CharSequence.partition(predicate: (Char) -> Boolean): Pair<CharSequence, CharSequence>(source)
```

```kotlin
fun main() {
    val text = "Hello123World456"
    val (digits, others) = text.partition { it.isDigit() }

    println("Digits  : $digits")   // 123456
    println("Others : $others")   // HelloWorld
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/partition.html)

    