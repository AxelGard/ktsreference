

# also

 [kotlin-stdlib](/kotlin-stdlib) / [kotlin](/kotlin-stdlib/kotlin) / [also](kotlin-stdlib/kotlin/also)

Calls the specified function block with this value as its argument and returns this value.

```kotlin
@IgnorableReturnValueinline fun <T> T.also(block: (T) -> Unit): T(source)
```

```kotlin
fun main() {
    val numbers = mutableListOf(1, 2, 3).also { println("Original list: $it") }
    numbers.add(4).also { println("After adding 4: $it") }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/also.html)

    