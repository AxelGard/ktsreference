

# apply

Calls the specified function block with this value as its receiver and returns this value.

```kotlin
@IgnorableReturnValueinline fun <T> T.apply(block: T.() -> Unit): T(source)
```

val numbers = mutableListOf<Int>().apply {
    add(10)
    add(20)
    add(30)
}

println(numbers)

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/apply.html)

    